import hashlib

cases = []
case_id = 1


def add_case():
    """Module 1: Register a new forensic investigation case."""
    global case_id

    title = input("Enter case title: ").strip()
    description = input("Enter case description: ").strip()

    case = {
        "id": case_id,
        "title": title,
        "description": description,
        "evidence": []
    }

    cases.append(case)
    print(f"Case successfully created! Assigned Case ID: {case_id}")
    case_id += 1


def add_evidence():
    """Module 2: Log evidence and seal it with SHA-256."""
    try:
        number = int(input("Enter Case ID to attach evidence: "))
    except ValueError:
        print("Invalid input! Case ID must be an integer.")
        return

    for case in cases:
        if case["id"] == number:
            evidence_desc = input("Enter evidence description (e.g., Device/Serial No.): ").strip()
            
            # Compute SHA-256 cryptographic fingerprint
            fingerprint = hashlib.sha256(evidence_desc.encode("utf-8")).hexdigest()

            item = {
                "description": evidence_desc,
                "fingerprint": fingerprint
            }

            case["evidence"].append(item)
            print("Evidence successfully sealed and appended to case dossier!")
            print(f"SHA-256 Seal: {fingerprint}")
            return

    print("Error: Case ID not found.")


def view_cases():
    """Module 3: View all active cases and seized artifacts."""
    if not cases:
        print("No cases currently on record.")
        return

    print("\n================ ACTIVE CASE DOSSIERS ================")
    for case in cases:
        print(f"\nCase ID     : {case['id']}")
        print(f"Title       : {case['title']}")
        print(f"Description : {case['description']}")
        print(f"Exhibits    : {len(case['evidence'])} item(s)")

        for idx, item in enumerate(case["evidence"], start=1):
            print(f"  [{idx}] {item['description']}")
            print(f"      Seal: {item['fingerprint']}")
    print("======================================================")


def verify_evidence():
    """Module 4: Recalculate hash and verify evidence integrity."""
    try:
        number = int(input("Enter Case ID to audit: "))
    except ValueError:
        print("Invalid input! Case ID must be an integer.")
        return

    for case in cases:
        if case["id"] == number:
            if not case["evidence"]:
                print("No evidence artifacts registered under this case.")
                return

            print(f"\n--- Auditing Case {case['id']}: {case['title']} ---")
            all_intact = True

            for idx, item in enumerate(case["evidence"], start=1):
                recomputed_hash = hashlib.sha256(item["description"].encode("utf-8")).hexdigest()

                if recomputed_hash == item["fingerprint"]:
                    print(f"  Exhibit [{idx}]: INTEGRITY VERIFIED (Match)")
                else:
                    print(f"  Exhibit [{idx}]: TAMPER DETECTED (Mismatch!)")
                    all_intact = False

            if all_intact:
                print("STATUS: 100% PASS - All evidence items authentic.")
            else:
                print("STATUS: ALERT - Integrity breach detected!")
            return

    print("Error: Case ID not found.")


def main():
    while True:
        print("\n=== DIGITAL FORENSIC EVIDENCE SYSTEM ===")
        print("1. Add New Case")
        print("2. Add Evidence to Case")
        print("3. View All Cases")
        print("4. Verify Evidence Integrity")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_case()
        elif choice == "2":
            add_evidence()
        elif choice == "3":
            view_cases()
        elif choice == "4":
            verify_evidence()
        elif choice == "5":
            print("System session terminated. Exiting...")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
