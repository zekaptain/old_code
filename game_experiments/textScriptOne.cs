using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class textScriptOne : MonoBehaviour {

	public Text text;
	bool t;

	// Use this for initialization
	void Start () {

	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown (KeyCode.T)) {
			text.text = "Space key pressed";
			t = true;
		}

	}
}
