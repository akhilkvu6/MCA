package com.example.activity_life_cycle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "Appstate";
    private TextView tvState;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvState = findViewById(R.id.tvState);
        updateStatus("Created");
    }

    @Override
    protected void onStart() {
        super.onStart();
        updateStatus("Starting");
    }

    @Override
    protected void onResume() {
        super.onResume();
        updateStatus("Resuming");
    }

    @Override
    protected void onPause() {
        super.onPause();
        updateStatus("Paused");
    }

    @Override
    protected void onStop() {
        super.onStop();
        updateStatus("Stopped");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        updateStatus("Restarted");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        updateStatus("Destroyed");
    }

    private void updateStatus(String state) {
        Log.d(TAG, state);
        Toast.makeText(this, state, Toast.LENGTH_SHORT).show();
        if (tvState != null) {
            tvState.setText("Current State: " + state);
        }
    }
}
