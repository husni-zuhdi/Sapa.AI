package com.project.sapaai.ui

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.setupActionBarWithNavController
import androidx.navigation.ui.setupWithNavController
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.*
import com.project.sapaai.R
import com.project.sapaai.ui.form.FormActivity
import com.project.sapaai.ui.home_form_profile.dashboard.DashboardFragment
import com.project.sapaai.ui.login_register.LoginActivity
import com.project.sapaai.ui.login_register.RegisterActivity
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_profile.*
import kotlinx.android.synthetic.main.activity_profile.fieldEmail

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

        supportActionBar?.hide()
        viewUsers()

    }

    private fun viewUsers() {

        val user = auth.currentUser
        val dbDirect = dbDirect?.child(user?.uid!!)

        dbDirect?.addValueEventListener(object: ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {

                fieldUsername.text =snapshot.child("username").value.toString()
                fieldEmail.text =snapshot.child("email").value.toString()

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
        buttonHome.setOnClickListener{
            startActivity(Intent(this@ProfileActivity, HomeActivity::class.java))

        }
        buttonPost.setOnClickListener{
            startActivity(Intent(this@ProfileActivity, DashboardFragment::class.java))

        }
        buttonProfile.setOnClickListener{
            startActivity(Intent(this@ProfileActivity, ProfileActivity::class.java))

        }
    }
}