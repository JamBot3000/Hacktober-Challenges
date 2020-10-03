const Fs = require("fs"),
	Gm = require("gm");

// INCLUDE THE ASCII GRAY SCALE JSON
var asciiScale = Fs.readFileSync("./ascii_val.json")
asciiScale = JSON.parse(asciiScale);

// OPEN AND MANIPULATE THE IMAGE
function open_img(imageData){
	imgSize = undefined;
	Gm(imageData.path) // OPEN THE IMAGE
		.colorspace("Gray") // REMOVE THE COLORS
		.resize(imageData.width, undefined) // REZISE TO BETTER PERFORMANCE
		.bitdepth(imageData.depth) // ADJUST THE COLORS
		.toBuffer("PNG", function(err, buffer){ // THEN PASS TO BUFFER
			if(err) throw err;
			// GET THE WIDTH AND HEIGHT
			Gm(buffer).size(function(err, size){
				if(err) throw err;
				let nhei = size.height - Math.floor(size.height/2);
				imgSize = size;
				imgSize.height = nhei;
				// GET THE NEW BUFFER
				Gm(buffer).resize(size.width, nhei, "!")
				.toBuffer("Gray", function(err, nbuffer){
					if(err) throw err;
					// AND PRINT IT
					print_ascii_image(nbuffer, imgSize);
				});
			});
		});
};

// PRINT THE ASCII IMAGE
function print_ascii_image(buffer, imgSize){
	let arrayImg = []; 
	// LOOP OVER THE BUFFER
	for(let i = 0; i < imgSize.height; i++){
		arrayImg.push("");
		for(let j = 0; j < imgSize.width; j++){
			let buffPos = j + (i * imgSize.width);
			let grayVal = buffer.readUInt8(buffPos);
			grayVal -= grayVal % 17;
			arrayImg[i] += asciiScale[grayVal + ""];
		}
	}
	for(let i = 0; i < arrayImg.length; i++){
		console.log(arrayImg[i]);
	}
};

// MAIN FUNCTION ------------------------------------------

class mArgs{
	path = undefined;
	width = 50;
	depth = 8;
	constructor(args){
		if(args.length < 1)
			throw ("ERR: No arguments");
		this.path = args[0];
		this.width = (args[1])? parseInt(args[1]) : this.width;
		this.depth = (args[2])? parseInt(args[2]) : this.depth;
	}
}

function main(){
	let args = new mArgs(process.argv.slice(2));
	open_img(args);
}; main();
