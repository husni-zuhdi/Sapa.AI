package com.project.sapaai.ui.login

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.project.sapaai.R
import com.project.sapaai.ui.HomeActivity

class LoginActivity : AppCompatActivity() {
    private lateinit var button: Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        button = findViewById(R.id.buttonSignIn)
        button.setOnClickListener{
            startActivity(Intent(this, HomeActivity::class.java))
        }
    }
}