{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cb7a2c9c-7021-4d02-b3ab-f54dacc7bd4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page fetched successfully. Status Code: 200\n",
      "b1only.txt has been saved.\n"
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
    "print(f\"Page fetched successfully. Status Code: {response.status_code}\")\n",
    "\n",
    "# Parse the HTML content\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Find all tables with class 'wikitable'\n",
    "launch_tables = soup.find_all('table', {'class': 'wikitable'})\n",
    "\n",
    "# List to hold the launch data for b1only\n",
    "b1only_data = []\n",
    "\n",
    "# Iterate through tables to find relevant data\n",
    "for table in launch_tables:\n",
    "    rows = table.find_all('tr')[1:]  # Skip header row\n",
    "    for row in rows:\n",
    "        columns = row.find_all('td')\n",
    "        if len(columns) > 7:\n",
    "            version = columns[1].text.strip()\n",
    "            if 'v1.0' in version or 'v1.1' in version:  # Only Block 1 (or Block 1.1)\n",
    "                serial_number = columns[0].text.strip()\n",
    "                launch_date = columns[2].text.strip()\n",
    "                flight_no = columns[3].text.strip()\n",
    "                payload = columns[4].text.strip()\n",
    "                launch_pad = columns[5].text.strip()\n",
    "                landing_location = columns[6].text.strip()\n",
    "                fate = columns[7].text.strip()\n",
    "                turnaround_time = columns[8].text.strip() if len(columns) > 8 else 'N/A'\n",
    "\n",
    "                # Add the captured data to the list\n",
    "                b1only_data.append({\n",
    "                    'Serial Number': serial_number,\n",
    "                    'Version': version,\n",
    "                    'Launch Date': launch_date,\n",
    "                    'Flight Number': flight_no,\n",
    "                    'Payload': payload,\n",
    "                    'Launch Pad': launch_pad,\n",
    "                    'Landing Location': landing_location,\n",
    "                    'Fate': fate,\n",
    "                    'Turnaround Time': turnaround_time,\n",
    "                })\n",
    "\n",
    "# Save the extracted data to a text file (b1only.txt)\n",
    "if b1only_data:\n",
    "    with open('b1only.txt', 'w') as file:\n",
    "        for entry in b1only_data:\n",
    "            file.write(str(entry) + '\\n')\n",
    "    print(\"b1only.txt has been saved.\")\n",
    "else:\n",
    "    print(\"No data to save for b1only.txt.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d3ec258-483e-4abb-8eef-ff72007d1712",
   "metadata": {},
   "outputs": [],
   "source": []
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
