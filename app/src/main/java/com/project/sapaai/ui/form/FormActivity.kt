package com.project.sapaai.ui.form

import android.app.ProgressDialog
import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.storage.FirebaseStorage
import com.project.sapaai.R
import com.project.sapaai.databinding.ActivityFormBinding
import kotlinx.android.synthetic.main.activity_form.*
import java.text.SimpleDateFormat
import java.util.*

class FormActivity  : AppCompatActivity(), View.OnClickListener{

    private lateinit var etKorban : EditText
    private lateinit var etPelaku : EditText
    private lateinit var etKronologi : EditText
    private lateinit var btnForm : Button
    lateinit var binding : ActivityFormBinding
    lateinit var photoUri : Uri

      override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_form)
          binding = ActivityFormBinding.inflate(layoutInflater)
          setContentView(binding.root)

          binding.addPhoto.setOnClickListener{
              addPhoto()
          }
          binding.uploadPhoto.setOnClickListener{
              uploadPhoto()
          }
        etKorban = findViewById(R.id.fieldKorban)
        etPelaku = findViewById(R.id.fieldPelaku)
        etKronologi = findViewById(R.id.fieldKronologi)
        btnForm = findViewById(R.id.buttonForm)

        btnForm.setOnClickListener(this)


    }

    private fun uploadPhoto() {
        val task = ProgressDialog(this)
        task.setMessage("uploading")
        task.setCancelable(false)
        task.show()

        val set = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault())
        val photoName = set.format(Date())
        val storageReference = FirebaseStorage.getInstance().getReference("photos/$photoName")

        storageReference.putFile(photoUri).
        addOnSuccessListener {
            binding.photoPreview.setImageURI(null)
            Toast.makeText(this@FormActivity,"sucess",Toast.LENGTH_SHORT).show()
            if (task.isShowing)task.dismiss()
        }.addOnFailureListener{
            if (task.isShowing)task.dismiss()
            Toast.makeText(this@FormActivity,"fail",Toast.LENGTH_SHORT).show()
        }
    }

    private fun addPhoto() {
        val intent = Intent()
        intent.type = "image/*"
        intent.action = Intent.ACTION_GET_CONTENT

        startActivityForResult(intent,100)
    }

    override fun onClick(v: View?) {
        saveData()

    }

    private fun saveData(){
        val Nkorban: String = etKorban.text.toString().trim()
        val Ntersangka : String = etPelaku.text.toString().trim()
        val Nkronologi : String = etKronologi.text.toString().trim()

        if(Nkorban.isEmpty()){
            etKorban.error = "isi nama korban!"
            return
        }
        if(Ntersangka.isEmpty()){
            etKronologi.error = "isi detail kronologi!"
            return
        }
        if(Nkronologi.isEmpty()){
            etKronologi.error = "isi nama tersangka!"
            return
        }
        val ref : DatabaseReference = FirebaseDatabase.getInstance().getReference("forms")
        val userId = ref.push().key
        val form = Form(userId!!,Nkorban,Ntersangka,Nkronologi)

        if (userId != null){
            ref.child(userId).setValue(form).addOnCompleteListener{
                Toast.makeText(applicationContext, "Data berhasil", Toast.LENGTH_SHORT).show()

            }
        }
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode==100 && resultCode == RESULT_OK ){
            photoUri = data?.data!!
            binding.photoPreview.setImageURI(photoUri)
        }
    }




}