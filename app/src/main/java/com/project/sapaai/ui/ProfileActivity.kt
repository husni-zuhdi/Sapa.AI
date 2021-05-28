package com.project.sapaai.ui

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.*
import com.project.sapaai.R
import com.project.sapaai.ui.form.FormActivity
import com.project.sapaai.ui.login_register.LoginActivity
import kotlinx.android.synthetic.main.activity_profile.*

class ProfileActivity : AppCompatActivity() {
    lateinit var auth: FirebaseAuth
    var dbDirect :  DatabaseReference? = null
    var database: FirebaseDatabase? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_profile)

        auth = FirebaseAuth.getInstance()
        database = FirebaseDatabase.getInstance()
        dbDirect = database?.reference!!.child("users")

        viewUsers()
    }

    private fun viewUsers() {

        val user = auth.currentUser
        val dbDirect = dbDirect?.child(user?.uid!!)

        dbDirect?.addValueEventListener(object: ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {

                fieldUsername.text ="Username = "+snapshot.child("username").value.toString()
                fieldEmail.text = "Email  = "+snapshot.child("email").value.toString()

            }

            override fun onCancelled(error: DatabaseError) {
                //
            }
        })


        logoutButton.setOnClickListener {
            auth.signOut()
            startActivity(Intent(this@ProfileActivity, LoginActivity::class.java))
            finish()
        }


    }
}