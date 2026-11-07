package com.example.implicit_intent;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button website, phone, email, maps, share, sms;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        website = findViewById(R.id.website);
        phone = findViewById(R.id.phone);
        email = findViewById(R.id.email);
        maps = findViewById(R.id.maps);
        share = findViewById(R.id.share);
        sms = findViewById(R.id.sms);

        // Open Website (College of Engineering Trivandrum)
        website.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.cet.ac.in"));
                    startActivity(intent);
                    Toast.makeText(MainActivity.this, "Opening CET Website...", Toast.LENGTH_SHORT).show();
                } catch (ActivityNotFoundException e) {
                    Toast.makeText(MainActivity.this, "No browser found", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Open Phone Dialer
        phone.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:9876543210"));
                    startActivity(intent);
                    Toast.makeText(MainActivity.this, "Opening Phone Dialer...", Toast.LENGTH_SHORT).show();
                } catch (ActivityNotFoundException e) {
                    Toast.makeText(MainActivity.this, "No dialer found", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Open Email
        email.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    Intent intent = new Intent(Intent.ACTION_SENDTO);
                    intent.setData(Uri.parse("mailto:example@cet.ac.in"));
                    intent.putExtra(Intent.EXTRA_SUBJECT, "MCA Lab Query");
                    intent.putExtra(Intent.EXTRA_TEXT, "Hello from Implicit Intent App!");
                    startActivity(intent);
                    Toast.makeText(MainActivity.this, "Opening Email App...", Toast.LENGTH_SHORT).show();
                } catch (ActivityNotFoundException e) {
                    Toast.makeText(MainActivity.this, "No email client found", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Open Maps (College of Engineering Trivandrum coordinates)
        maps.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("geo:8.5458,76.9063?q=College+of+Engineering+Trivandrum"));
                    startActivity(intent);
                    Toast.makeText(MainActivity.this, "Opening Maps...", Toast.LENGTH_SHORT).show();
                } catch (ActivityNotFoundException e) {
                    Toast.makeText(MainActivity.this, "No maps app found", Toast.LENGTH_SHORT).show();
                }
            }
        });

        // Share Text
        share.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_SEND);
                intent.setType("text/plain");
                intent.putExtra(Intent.EXTRA_TEXT, "Hello from Android Implicit Intent experiment!");
                startActivity(Intent.createChooser(intent, "Share via"));
            }
        });

        // Open SMS
        sms.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    Intent intent = new Intent(Intent.ACTION_SENDTO, Uri.parse("smsto:9876543210"));
                    intent.putExtra("sms_body", "Hello from Implicit Intent App");
                    startActivity(intent);
                    Toast.makeText(MainActivity.this, "Opening SMS...", Toast.LENGTH_SHORT).show();
                } catch (ActivityNotFoundException e) {
                    Toast.makeText(MainActivity.this, "No SMS app found", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
