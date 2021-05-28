package com.project.sapaai.ui.form

data class Form(
    val id: String,
    val nama_korban: String,
    val nama_pelaku: String) {
    constructor() : this(
        "", "", "")
}