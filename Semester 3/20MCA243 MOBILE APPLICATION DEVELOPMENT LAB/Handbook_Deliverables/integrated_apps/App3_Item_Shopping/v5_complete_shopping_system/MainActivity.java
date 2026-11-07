package com.example.integrated.app3.v5;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    Spinner spProduct;
    EditText etQuantity;
    Button btnAdd, btnCheckout;
    ListView lvCart;
    TextView tvGrandTotal;

    String[] products = {"Android Textbook ($50)", "Stylus Pen ($20)", "Tablet Stand ($30)", "USB-C Cable ($10)"};
    int[] prices = {50, 20, 30, 10};

    ArrayList<String> cartItems = new ArrayList<>();
    ArrayAdapter<String> adapter;
    int grandTotal = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        spProduct = findViewById(R.id.spProduct);
        etQuantity = findViewById(R.id.etQuantity);
        btnAdd = findViewById(R.id.btnAdd);
        btnCheckout = findViewById(R.id.btnCheckout);
        lvCart = findViewById(R.id.lvCart);
        tvGrandTotal = findViewById(R.id.tvGrandTotal);

        ArrayAdapter<String> prodAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, products);
        spProduct.setAdapter(prodAdapter);

        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, cartItems);
        lvCart.setAdapter(adapter);

        btnAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String qtyStr = etQuantity.getText().toString().trim();
                if (qtyStr.isEmpty()) {
                    etQuantity.setError("Enter quantity");
                    return;
                }
                int qty = Integer.parseInt(qtyStr);
                int selectedIdx = spProduct.getSelectedItemPosition();
                int itemCost = prices[selectedIdx] * qty;
                grandTotal += itemCost;

                String entry = products[selectedIdx] + " x " + qty + " = $" + itemCost;
                cartItems.add(entry);
                adapter.notifyDataSetChanged();
                tvGrandTotal.setText("Total: $" + grandTotal);
                etQuantity.setText("");
            }
        });

        btnCheckout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (cartItems.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Cart is empty", Toast.LENGTH_SHORT).show();
                    return;
                }
                Intent intent = new Intent(MainActivity.this, OrderSummaryActivity.class);
                intent.putStringArrayListExtra("ITEMS", cartItems);
                intent.putExtra("TOTAL", grandTotal);
                startActivity(intent);
            }
        });
    }
}