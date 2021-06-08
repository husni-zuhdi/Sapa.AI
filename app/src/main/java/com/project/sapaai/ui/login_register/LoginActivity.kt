package com.project.sapaai.ui.login_register

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.TextUtils
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.project.sapaai.ui.ProfileActivity
import com.project.sapaai.R
import com.project.sapaai.ui.HomeActivity
import kotlinx.android.synthetic.main.activity_login.*

class LoginActivity : AppCompatActivity() {
    lateinit var auth: FirebaseAuth
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)


        auth = FirebaseAuth.getInstance()

        val personDirect = auth.currentUser
        if(personDirect != null) {
            startActivity(Intent(this@LoginActivity, HomeActivity::class.java))
            finish()
        }
        login()
    }

    private fun login() {

        buttonSignIn.setOnClickListener {

            if(TextUtils.isEmpty(fieldEmail.text.toString())){
                fieldEmail.error = "username"
                return@setOnClickListener
            }
            else if(TextUtils.isEmpty(fieldPassword.text.toString())){
                fieldEmail.error = "password"
                return@setOnClickListener
            }
            auth.signInWithEmailAndPassword(fieldEmail.text.toString(), fieldPassword.text.toString())
                .addOnCompleteListener {
                    if(it.isSuccessful) {
                        startActivity(Intent(this@LoginActivity, HomeActivity::class.java))
                        finish()
                    } else {
                        Toast.makeText(this@LoginActivity, "Login failed", Toast.LENGTH_LONG).show()
                    }
                }

        }

        tv_register.setOnClickListener{
            startActivity(Intent(this@LoginActivity, RegisterActivity::class.java))

        }
    }

}