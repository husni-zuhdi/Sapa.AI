package com.project.sapaai.ui.call

import android.Manifest
import android.content.pm.PackageManager
import android.media.MediaRecorder
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.view.View
import android.widget.Toast
import androidx.core.app.ActivityCompat
import com.google.firebase.storage.FirebaseStorage
import com.google.firebase.storage.StorageReference
import com.project.sapaai.R
import com.project.sapaai.databinding.ActivityCallBinding
import java.io.File
import java.text.SimpleDateFormat
import java.util.*

class CallActivity : AppCompatActivity() {

    lateinit var binding: ActivityCallBinding
    lateinit var mr: MediaRecorder
    lateinit var storage: StorageReference
    lateinit var path: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_call)
        binding = ActivityCallBinding.inflate(layoutInflater)
        setContentView(binding.root)

        path = Environment.getExternalStorageDirectory().toString()+"/myrecaudio.mp3"

        storage = FirebaseStorage.getInstance().reference

        supportActionBar?.title = "Call Report"

        if(ActivityCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.RECORD_AUDIO,
                                                                    Manifest.permission.WRITE_EXTERNAL_STORAGE), 111)

        binding.callIvRekam.setOnClickListener {
            mr = MediaRecorder()
            mr.setAudioSource(MediaRecorder.AudioSource.MIC)
            mr.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            mr.setAudioEncoder(MediaRecorder.OutputFormat.MPEG_4)
            mr.setOutputFile(path)
            mr.prepare()
            mr.start()
            binding.callIvRekam.visibility = View.GONE
            binding.callIvStop.visibility = View.VISIBLE
        }

        binding.callIvStop.setOnClickListener {
            mr.stop()
            mr.reset()
            mr.release()
            uploadAudio()
            binding.callIvStop.visibility = View.GONE
            binding.callIvRekam.visibility = View.VISIBLE
        }

    }

    fun uploadAudio(){
//        val filepath = storage.child("recorded-voice").child("new_audio.3gp")
        val set = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault())
        val audioFile = set.format(Date())
        val storageReference = FirebaseStorage.getInstance().getReference("recorded-voice/$audioFile.mp3")

        val uri = Uri.fromFile(File(path))

        storageReference.putFile(uri).
        addOnSuccessListener {
            Toast.makeText(this@CallActivity,"sucess",Toast.LENGTH_SHORT).show()
        }.addOnFailureListener{
            Toast.makeText(this@CallActivity,"fail",Toast.LENGTH_SHORT).show()
        }

//        val uri = Uri.fromFile(File(path))
//        filepath.putFile(uri).addOnSuccessListener {
//            Toast.makeText(
//                this@CallActivity,
//                "Uploading Finished",
//                Toast.LENGTH_SHORT
//            ).show()
//        }
    }

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if(requestCode==111 && grantResults[0] == PackageManager.PERMISSION_GRANTED)
            binding.callIvRekam.isEnabled = true
    }
}