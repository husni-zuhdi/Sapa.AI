package com.project.sapaai.ui.home_form_profile.home

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.ViewFlipper
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import com.project.sapaai.R
import com.project.sapaai.databinding.FragmentHomeBinding
import com.project.sapaai.ui.call.CallActivity


class HomeFragment : Fragment() {

    private lateinit var homeViewModel: HomeViewModel
    private lateinit var binding: FragmentHomeBinding
    private lateinit var flipper: ViewFlipper

    var gallery_grid_Images = intArrayOf(R.drawable.education, R.drawable.education2, R.drawable.education3
    )


    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        homeViewModel =
            ViewModelProvider(this).get(HomeViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_home, container, false)

        binding = FragmentHomeBinding.inflate(layoutInflater, container, false)
//        flipper = binding.homeVlHanyauntukmu
//        for (i in 0 until gallery_grid_Images.size) {
//            // This will create dynamic image views and add them to the ViewFlipper.
//            setFlipperImage(gallery_grid_Images[i])
//        }

//        binding.homeFlCall.setOnClickListener {
//            Intent(context, CallActivity::class.java).also {
//                startActivity(it)
//            }
//        }

        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.homeFlCall.setOnClickListener {
                Intent(context, CallActivity::class.java).also {
                startActivity(it)
            }
        }

        flipper = binding.homeVlHanyauntukmu
        for (i in 0 until gallery_grid_Images.size) {
            // This will create dynamic image views and add them to the ViewFlipper.
            setFlipperImage(gallery_grid_Images[i])
        }
    }

    private fun setFlipperImage(res: Int) {
        Log.i("Set Filpper Called", res.toString() + "")
        val image = ImageView(context)
        image.setBackgroundResource(res)
        flipper.addView(image)
        flipper.setFlipInterval(5000)
        flipper.setAutoStart(true)
    }
}