package com.project.sapaai.ui.form

data class Form(
    val id: String,
    val nama_korban: String,
    val nama_pelaku: String,
    val flag_layanan1: String,
    val flag_layanan2: String,
    val flag_layanan3: String,
    val flag_layanan4: String,
    val flag_layanan5: String,
    val flag_layanan6: String,
    val flag_layanan7: String,
    val flag_layanan8: String,
    val kronologi_kejadian: String) {
    constructor() : this(
        "", "", "","","","","","","","","","")
}