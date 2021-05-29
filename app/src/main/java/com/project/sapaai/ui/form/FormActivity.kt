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
import com.project.sapaai.databinding.ActivityFormBinding
import java.text.SimpleDateFormat
import java.util.*

class FormActivity : AppCompatActivity(), View.OnClickListener,DatePickerFragment.DialogDateListener {
    private lateinit var etKorban : EditText
    private lateinit var etPelaku : EditText
    private lateinit var btnForm : Button

    private var binding: ActivityFormBinding? = null

    companion object {
        private const val DATE_PICKER_TAG = "DatePicker"
    }

    override fun onDialogDateSet(tag: String?, year: Int, month: Int, dayOfMonth: Int) {
        // Siapkan date formatter-nya terlebih dahulu
        val calendar = Calendar.getInstance()
        calendar.set(year, month, dayOfMonth)
        val dateFormat = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())

        // Set text dari textview once
        binding?.fieldDate?.text = dateFormat.format(calendar.time)
    }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_form)

        etKorban = findViewById(R.id.fieldKorban)
        etPelaku = findViewById(R.id.fieldPelaku)
        btnForm = findViewById(R.id.buttonForm)

        btnForm.setOnClickListener(this)

/*        binding = ActivityFormBinding.inflate(layoutInflater)
        setContentView(binding?.root)

        // Listener one time alarm
        binding?.btnOnceDate?.setOnClickListener(this)*/
    }
    override fun onClick(v: View?) {
        saveData()
        if (v != null) {
            when (v.id) {
                R.id.btn_once_date -> {
                    val datePickerFragment = DatePickerFragment()
                    datePickerFragment.show(supportFragmentManager, DATE_PICKER_TAG)
                }
            }
        }
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