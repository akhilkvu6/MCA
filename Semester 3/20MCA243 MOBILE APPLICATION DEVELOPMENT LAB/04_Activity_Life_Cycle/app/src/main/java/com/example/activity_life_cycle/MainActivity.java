package com.example.activity_life_cycle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.d("Appstate", "Created");
        Toast.makeText(this, "Created", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onStart() {
        super.onStart();

        Log.d("Appstate", "Starting");
        Toast.makeText(this, "Starting", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onResume() {
        super.onResume();

        Log.d("Appstate", "Resuming");
        Toast.makeText(this, "Resuming", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onPause() {
        super.onPause();

        Log.d("Appstate", "Paused");
        Toast.makeText(this, "Paused", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onStop() {
        super.onStop();

        Log.d("Appstate", "Stopped");
        Toast.makeText(this, "Stopped", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();

        Log.d("Appstate", "Restarted");
        Toast.makeText(this, "Restarted", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();

        Log.d("Appstate", "Destroyed");
        Toast.makeText(this, "Destroyed", Toast.LENGTH_SHORT).show();
    }
}