{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f1d5f213-46a6-41a6-a632-a0dbe485e9de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page fetched successfully. Status Code: 200\n",
      "b4only.txt has been saved.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# URL for Falcon 9 launch data\n",
    "url = 'https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters'\n",
    "response = requests.get(url)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    print(\"Page fetched successfully. Status Code:\", response.status_code)\n",
    "    soup = BeautifulSoup(response.content, 'html.parser')\n",
    "\n",
    "    # Find all the tables on the page\n",
    "    launch_tables = soup.find_all('table', {'class': 'wikitable'})\n",
    "    b4only_data = []\n",
    "\n",
    "    # Iterate through each table to extract Block 4 data\n",
    "    for table in launch_tables:\n",
    "        rows = table.find_all('tr')[1:]  # Skip header row\n",
    "        for row in rows:\n",
    "            columns = row.find_all('td')\n",
    "            if len(columns) > 7:\n",
    "                version = columns[1].text.strip().replace('\\xa0', ' ')  # Remove non-breaking spaces\n",
    "\n",
    "                if 'F9 B4' in version:  # Only Block 4 engines\n",
    "                    serial_number = columns[0].text.strip()\n",
    "                    launch_date = columns[2].text.strip()\n",
    "                    flight_no = columns[3].text.strip()\n",
    "                    payload = columns[4].text.strip()\n",
    "                    launch_pad = columns[5].text.strip()\n",
    "                    landing_location = columns[6].text.strip()\n",
    "                    fate = columns[7].text.strip()\n",
    "                    turnaround_time = columns[8].text.strip() if len(columns) > 8 else 'N/A'\n",
    "\n",
    "                    b4only_data.append({\n",
    "                        'Serial Number': serial_number,\n",
    "                        'Version': version,\n",
    "                        'Launch Date': launch_date,\n",
    "                        'Flight Number': flight_no,\n",
    "                        'Payload': payload,\n",
    "                        'Launch Pad': launch_pad,\n",
    "                        'Landing Location': landing_location,\n",
    "                        'Fate': fate,\n",
    "                        'Turnaround Time': turnaround_time,\n",
    "                    })\n",
    "\n",
    "    # Save the extracted data to a text file for Block 4\n",
    "    if b4only_data:\n",
    "        with open('b4only.txt', 'w') as file:\n",
    "            for entry in b4only_data:\n",
    "                file.write(str(entry) + '\\n')\n",
    "        print(\"b4only.txt has been saved.\")\n",
    "    else:\n",
    "        print(\"No data to save for b4only.txt.\")\n",
    "else:\n",
    "    print(f\"Failed to fetch the page. Status code: {response.status_code}\")\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
