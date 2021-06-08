package com.project.sapaai.ui.call

import android.net.Uri
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.storage.StorageReference
import java.io.File

class Test : AppCompatActivity() {
    private val mStorage: StorageReference? = null
    private val mFileName: String? = null
    fun uploadAudio() {
        val filepath = mStorage!!.child("Audio").child("new_audio.3gp")
        val uri = Uri.fromFile(File(mFileName))
        filepath.putFile(uri).addOnSuccessListener {
            Toast.makeText(
                this@Test,
                "Uploading Finished",
                Toast.LENGTH_SHORT
            ).show()
        }
    }
}