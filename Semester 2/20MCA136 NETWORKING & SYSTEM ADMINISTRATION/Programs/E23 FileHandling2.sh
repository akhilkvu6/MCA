#!/bin/bash

# 1. Create file
cat > myfile <<EOF
1001 RAM 97
1002 NEHA 89
1010 DIVYA 77
1025 RAHUL 65
1012 ARUN 99
1013 NISHA 76
EOF

echo "------------------------"

# 2. First 2 rows
echo "First 2 rows:"
head -2 myfile

echo "------------------------"

# 3. Last 2 rows
echo "Last 2 rows:"
tail -2 myfile

echo "------------------------"

# 4. Copy file
cp myfile mycopyfile
echo "File copied to mycopyfile"

echo "------------------------"

# 5. Count
echo "Lines: $(wc -l < myfile)"
echo "Words: $(wc -w < myfile)"
echo "Characters: $(wc -c < myfile)"

echo "------------------------"

# 6. 3rd row
echo "3rd row:"
sed -n '3p' myfile

echo "------------------------"

# 7. Append
cat myfile >> myappendfile
echo "Content appended to myappendfile"