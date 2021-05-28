package com.project.sapaai.ui.form

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.FirebaseDatabase
import com.project.sapaai.R

class FormActivity : AppCompatActivity(), View.OnClickListener {
    private lateinit var etKorban : EditText
    private lateinit var etPelaku : EditText
    private lateinit var btnForm : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_form)

        etKorban = findViewById(R.id.fieldKorban)
        etPelaku = findViewById(R.id.fieldPelaku)
        btnForm = findViewById(R.id.buttonForm)

        btnForm.setOnClickListener(this)
    }
    override fun onClick(v: View?) {
        saveData()
    }

    private fun saveData(){
        val Nkorban: String = etKorban.text.toString().trim()
        val Ntersangka : String = etPelaku.text.toString().trim()

        if(Nkorban.isEmpty()){
            etKorban.error = "isi nama korban!"
            return
        }
        if(Ntersangka.isEmpty()){
            etPelaku.error = "isi nama tersangka!"
            return
        }
        val ref : DatabaseReference = FirebaseDatabase.getInstance().getReference("forms")
        val userId = ref.push().key
        val form = Form(userId!!,Nkorban,Ntersangka)

        if (userId != null){
            ref.child(userId).setValue(form).addOnCompleteListener{
                Toast.makeText(applicationContext, "Data berhasil", Toast.LENGTH_SHORT).show()

            }
        }
    }




}