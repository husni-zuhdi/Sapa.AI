package com.project.sapaai.ui.login_register

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.TextUtils
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.project.sapaai.R
import kotlinx.android.synthetic.main.activity_register.*

class RegisterActivity : AppCompatActivity() {
    lateinit var auth: FirebaseAuth
    var dbDirect: DatabaseReference? = null
    var database: FirebaseDatabase? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)

        auth = FirebaseAuth.getInstance()
        database = FirebaseDatabase.getInstance()
        dbDirect = database?.reference!!.child("users")

        register()
    }

    private fun register() {


        buttonSignUp.setOnClickListener {

            if (TextUtils.isEmpty(fieldUsername.text.toString())) {
                fieldUsername
                return@setOnClickListener
            } else if (TextUtils.isEmpty(fieldFullname.text.toString())) {
                fieldUsername
                return@setOnClickListener
            } else if (TextUtils.isEmpty(fieldPhonenumber.text.toString())) {
                fieldUsername
                return@setOnClickListener
            } else if (TextUtils.isEmpty(fieldEmail.text.toString())) {
                fieldUsername
                return@setOnClickListener
            } else if (TextUtils.isEmpty(fieldPassword.text.toString())) {
                fieldUsername
                return@setOnClickListener
            }


            auth.createUserWithEmailAndPassword(
                fieldEmail.text.toString(),
                fieldPassword.text.toString()
            )
                .addOnCompleteListener {
                    if (it.isSuccessful) {
                        val currentUser = auth.currentUser
                        val rightDb = dbDirect?.child((currentUser?.uid!!))
                        rightDb?.child("username")
                            ?.setValue(fieldUsername.text.toString())
                        rightDb?.child("fullname")
                            ?.setValue(fieldFullname.text.toString())
                        rightDb?.child("Phone Number")
                            ?.setValue(fieldPhonenumber.text.toString())
                        rightDb?.child("email")
                            ?.setValue(fieldEmail.text.toString())

                        Toast.makeText(
                            this@RegisterActivity, "Registration Success. ",
                            Toast.LENGTH_SHORT
                        ).show()
                        finish()

                    } else {
                        Toast.makeText(
                            this@RegisterActivity, "Registration failed ",
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                }
        }

    }
}