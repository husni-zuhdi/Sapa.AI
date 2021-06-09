package com.project.sapaai.ui

import android.app.ProgressDialog
import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.*
import com.google.firebase.storage.FirebaseStorage
import com.project.sapaai.R
import com.project.sapaai.databinding.ActivityProfileBinding
import com.project.sapaai.ui.home_form_profile.help.HelpFragment
import com.project.sapaai.ui.login_register.LoginActivity
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_profile.*
import kotlinx.android.synthetic.main.activity_profile.fieldEmail
import java.text.SimpleDateFormat
import java.util.*

class ProfileActivity : AppCompatActivity() {
    lateinit var auth: FirebaseAuth
    var dbDirect :  DatabaseReference? = null
    var database: FirebaseDatabase? = null
    lateinit var binding : ActivityProfileBinding
    lateinit var photoUri : Uri

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_profile)
        binding = ActivityProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.addPhoto.setOnClickListener{
            addPhoto()
        }
        binding.uploadPhoto.setOnClickListener{
            uploadPhoto()
        }
        auth = FirebaseAuth.getInstance()
        database = FirebaseDatabase.getInstance()
        dbDirect = database?.reference!!.child("users")

        supportActionBar?.hide()
        viewUsers()

    }

    private fun uploadPhoto() {
        val task = ProgressDialog(this)
        task.setMessage("uploading")
        task.setCancelable(false)
        task.show()

        val formatter = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault())
        val photoName = formatter.format(Date())
        val storageReference = FirebaseStorage.getInstance().getReference("$photoName")

        storageReference.putFile(photoUri).
        addOnSuccessListener {
            binding.photoPreview.setImageURI(null)
            photoPreview.setImageURI(photoUri)
            Toast.makeText(this@ProfileActivity,"sucess", Toast.LENGTH_SHORT).show()
            if (task.isShowing)task.dismiss()
        }.addOnFailureListener{
            if (task.isShowing)task.dismiss()
            Toast.makeText(this@ProfileActivity,"fail", Toast.LENGTH_SHORT).show()
        }
    }

    private fun addPhoto() {
        val intent = Intent()
        intent.type = "image/*"
        intent.action = Intent.ACTION_GET_CONTENT

        startActivityForResult(intent,100)
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode==100 && resultCode == RESULT_OK ){
            photoUri = data?.data!!
            binding.photoPreview.setImageURI(photoUri)
        }
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
            startActivity(Intent(this@ProfileActivity, HelpFragment::class.java))

        }
        buttonProfile.setOnClickListener{
            startActivity(Intent(this@ProfileActivity, ProfileActivity::class.java))

        }
    }
}