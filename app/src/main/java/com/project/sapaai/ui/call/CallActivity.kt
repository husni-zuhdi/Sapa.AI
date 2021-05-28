package com.project.sapaai.ui.call

import android.Manifest
import android.content.pm.PackageManager
import android.media.MediaRecorder
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Environment
import android.view.View
import androidx.core.app.ActivityCompat
import com.project.sapaai.R
import com.project.sapaai.databinding.ActivityCallBinding

class CallActivity : AppCompatActivity() {

    lateinit var binding: ActivityCallBinding
    lateinit var mr: MediaRecorder

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_call)
        binding = ActivityCallBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.callIvRekam.isEnabled = false

        var path = Environment.getExternalStorageDirectory().toString()+"/myrecaudio.3gp"
        mr = MediaRecorder()

        supportActionBar?.title = "Call Report"

        if(ActivityCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.RECORD_AUDIO,
                                                                    Manifest.permission.WRITE_EXTERNAL_STORAGE), 111)

        binding.callIvRekam.setOnClickListener {
            mr.setAudioSource(MediaRecorder.AudioSource.MIC)
            mr.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP)
            mr.setAudioEncoder(MediaRecorder.OutputFormat.AMR_NB)
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
            binding.callIvStop.visibility = View.GONE
            binding.callIvRekam.visibility = View.VISIBLE
        }

    }

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if(requestCode==111 && grantResults[0] == PackageManager.PERMISSION_GRANTED)
            binding.callIvRekam.isEnabled = true
    }
}