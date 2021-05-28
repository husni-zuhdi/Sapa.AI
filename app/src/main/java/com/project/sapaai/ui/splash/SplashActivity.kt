package com.project.sapaai.ui.splash

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.view.Window
import android.view.WindowManager
import com.project.sapaai.R
import com.project.sapaai.ui.HomeActivity
import com.project.sapaai.ui.login_register.LoginActivity

class SplashActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            window.requestFeature(Window.FEATURE_NO_TITLE)
            window.setFlags(
                WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN
            )
            setContentView(R.layout.activity_splash)

            Handler().postDelayed({
                startActivity(Intent(this@SplashActivity, LoginActivity::class.java))
                finish()
            }, 4000)
        }
    }