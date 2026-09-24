package com.example.implicit_intent;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button website, phone, email, maps, share, sms;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        website = findViewById(R.id.website);
        phone = findViewById(R.id.phone);
        email = findViewById(R.id.email);
        maps = findViewById(R.id.maps);
        share = findViewById(R.id.share);
        sms = findViewById(R.id.sms);

        // Open Website
        website.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(Intent.ACTION_VIEW);
                intent.setData(Uri.parse("https://www.cet.ac.in"));
                startActivity(intent);

                Toast.makeText(MainActivity.this,
                        "Website Opened",
                        Toast.LENGTH_SHORT).show();
            }
        });

        // Open Phone Dialer
        phone.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(Intent.ACTION_DIAL);
                intent.setData(Uri.parse("tel:9876543210"));
                startActivity(intent);

                Toast.makeText(MainActivity.this,
                        "Phone Dialer Opened",
                        Toast.LENGTH_SHORT).show();
            }
        });

        // Open Email
        email.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(Intent.ACTION_SENDTO);
                intent.setData(Uri.parse("mailto:example@gmail.com"));
                intent.putExtra(Intent.EXTRA_SUBJECT, "Test Email");
                intent.putExtra(Intent.EXTRA_TEXT, "Hello");

                startActivity(intent);

                Toast.makeText(MainActivity.this,
                        "Email App Opened",
                        Toast.LENGTH_SHORT).show();
            }
        });

        // Open Maps
        maps.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(
                        Intent.ACTION_VIEW,
                        Uri.parse("geo:8.5241,76.9366")
                );

                startActivity(intent);

                Toast.makeText(MainActivity.this,
                        "Maps Opened",
                        Toast.LENGTH_SHORT).show();
            }
        });

        // Share Text
        share.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(Intent.ACTION_SEND);
                intent.setType("text/plain");
                intent.putExtra(
                        Intent.EXTRA_TEXT,
                        "Hello from Implicit Intent App"
                );

                startActivity(
                        Intent.createChooser(intent, "Share Using")
                );

                Toast.makeText(MainActivity.this,
                        "Share Menu Opened",
                        Toast.LENGTH_SHORT).show();
            }
        });

        // Open SMS
        sms.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(Intent.ACTION_SENDTO);
                intent.setData(Uri.parse("smsto:9876543210"));
                intent.putExtra(
                        "sms_body",
                        "Hello from Implicit Intent App"
                );

                startActivity(intent);

                Toast.makeText(MainActivity.this,
                        "SMS App Opened",
                        Toast.LENGTH_SHORT).show();
            }
        });
    }
}