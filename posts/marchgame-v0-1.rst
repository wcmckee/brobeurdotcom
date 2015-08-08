<html><head></head><body><p>
BroBeur Studios | MarchGame

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script><script type="text/javascript">// <![CDATA[

var unityObjectUrl = "http://webplayer.unity3d.com/download_webplayer-3.x/3.0/uo/UnityObject2.js";
		if (document.location.protocol == 'https:')
			unityObjectUrl = unityObjectUrl.replace("http://", "https://ssl-");
		document.write('<script type="text\/javascript" src="' + unityObjectUrl + '"><\/script>');
// ]]></script>

<script type="text/javascript">// <![CDATA[

var config = { 				width: 512,  				height: 512, 				params: { enableDebugging:"0" } 				 			}; 			var u = new UnityObject2(config); 			jQuery(function() { 				var $missingScreen = jQuery("#unityPlayer").find(".missing"); 				var $brokenScreen = jQuery("#unityPlayer").find(".broken"); 				$missingScreen.hide(); 				$brokenScreen.hide(); 				 				u.observeProgress(function (progress) { 					switch(progress.pluginStatus) { 						case "broken": 							$brokenScreen.find("a").click(function (e) { 								e.stopPropagation(); 								e.preventDefault(); 								u.installPlugin(); 								return false; 							}); 							$brokenScreen.show(); 						break; 						case "missing": 							$missingScreen.find("a").click(function (e) { 								e.stopPropagation(); 								e.preventDefault(); 								u.installPlugin(); 								return false; 							}); 							$missingScreen.show(); 						break; 						case "installed": 							$missingScreen.remove(); 						break; 						case "first": 						break; 					} 				}); 				u.initPlugin(jQuery("#unityPlayer")[0], "march-game-0.unity3d"); 			});

// ]]></script>



<style type="text/css"><!--

body { 			font-family: Helvetica, Verdana, Arial, sans-serif; 			background-color: white; 			color: black; 			text-align: center; 		} 		a:link, a:visited { 			color: #000; 		} 		a:active, a:hover { 			color: #666; 		} 		p.header { 			font-size: small; 		} 		p.header span { 			font-weight: bold; 		} 		p.footer { 			font-size: x-small; 		} 		div.content { 			margin: auto; 			width: 960px; 		} 		div.broken, 		div.missing { 			margin: auto; 			position: relative; 			top: 50%; 			width: 193px; 		} 		div.broken a, 		div.missing a { 			height: 63px; 			position: relative; 			top: -31px; 		} 		div.broken img, 		div.missing img { 			border-width: 0px; 		} 		div.broken { 			display: none; 		} 		div#unityPlayer { 			cursor: default; 			height: 600px; 			width: 960px; 		} 		-->

--></style> 

</p><p class="header"><span> </span></p>



<h1 style="font-family: monospace; color: #d9af3e; font-size: 48px; text-align: center;">BroBeur Studios</h1>

<h2 style="font-family: monospace; color: #b7a676; font-size: 24px; text-align: center;">MarchGame v0.1 Third person platformer.</h2>

<h3 style="font-family: monospace; color: #b7a676; font-size: 24px; text-align: center;"><a href="http://brobeur.com">home</a> <a href="http://brobeur.com/about/">about</a> <a href="http://brobeur.com/sign-up/">sign-up</a>

<a href="http://brobeur.com/random/">random</a></h3>

 

<p class="header">MarchGame v0.1</p>

<p class="header"></p>

<p class="header"><a href="/wp-content/uploads/2013/04/marchGame-1.png"><img class="alignnone size-medium wp-image-65" alt="marchGame-1" src="/wp-content/uploads/2013/04/marchGame-1-300x300.png" width="300" height="300"></a></p>



<div class="content">

<div id="unityPlayer">

<div class="missing"><a title="Unity Web Player. Install now!" href="http://unity3d.com/webplayer/">

<img alt="Unity Web Player. Install now!" src="http://webplayer.unity3d.com/installation/getunity.png" width="193" height="63">

</a></div>

<div class="broken"><a title="Unity Web Player. Install now! Restart your browser after install." href="http://unity3d.com/webplayer/">

<img alt="Unity Web Player. Install now! Restart your browser after install." src="http://webplayer.unity3d.com/installation/getunityrestart.png" width="193" height="63">

</a></div>

</div>

</div>

<p class="footer">« created with <a title="Go to unity3d.com" href="http://unity3d.com/unity/">Unity</a> »</p>

 </body></html>