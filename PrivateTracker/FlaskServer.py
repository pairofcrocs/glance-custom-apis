from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database with a single-row structure
def init_db():
    conn = sqlite3.connect('tracker_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tracker (
                        red_ratio TEXT,
                        red_class TEXT,
                        red_messages TEXT,
                        btn_lumens TEXT,
                        btn_bp TEXT,
                        btn_hnr TEXT,
                        btn_messages TEXT,
                        ggn_ratio TEXT,
                        ggn_gold TEXT,
                        ggn_messages TEXT,
                        ptp_bonus TEXT,
                        ptp_message TEXT,
                        ptp_ratio TEXT)''')

    # Ensure only one row exists
    cursor.execute('SELECT COUNT(*) FROM tracker')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO tracker DEFAULT VALUES')  # Creates an empty row
    conn.commit()
    conn.close()

# Route to get tracker data
@app.route("/get-tracker", methods=["GET"])
def get_tracker():
    conn = sqlite3.connect('tracker_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tracker')
    row = cursor.fetchone()
    conn.close()

    if row:
        keys = ["red_ratio", "red_class", "red_messages", "btn_lumens", "btn_bp", "btn_hnr", 
                "btn_messages", "ggn_ratio", "ggn_gold", "ggn_messages", "ptp_bonus", "ptp_message", "ptp_ratio"]
        tracker_data = dict(zip(keys, row))
        return jsonify(tracker_data), 200
    else:
        return jsonify({"error": "Tracker data not found"}), 404

# Route to update tracker data (overwrite existing row)
@app.route("/update-tracker", methods=["POST"])
def update_tracker():
    data = request.get_json()

    conn = sqlite3.connect('tracker_data.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE tracker SET 
                      red_ratio = ?, red_class = ?, red_messages = ?, btn_lumens = ?, btn_bp = ?, 
                      btn_hnr = ?, btn_messages = ?, ggn_ratio = ?, ggn_gold = ?, ggn_messages = ?, 
                      ptp_bonus = ?, ptp_message = ?, ptp_ratio = ?''',
                   (data.get('red_ratio', ''), data.get('red_class', ''), data.get('red_messages', ''),
                    data.get('btn_lumens', ''), data.get('btn_bp', ''), data.get('btn_hnr', ''),
                    data.get('btn_messages', ''), data.get('ggn_ratio', ''), data.get('ggn_gold', ''),
                    data.get('ggn_messages', ''), data.get('ptp_bonus', ''), data.get('ptp_message', ''),
                    data.get('ptp_ratio', '')))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Tracker data updated successfully"}), 200

if __name__ == "__main__":
    init_db()  # Initialize the database
    app.run(host='0.0.0.0', port=2840)
