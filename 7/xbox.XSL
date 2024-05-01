<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">
<html>
<head>
<style>

      *{
			margin: 0;
			padding: 0;
			font-family: Calibri;
			font-color:white;
		}
		body{
            background: radial-gradient(#fff,#ff6f61);
            width:100%; 
            height: 100vh;
            background-size: cover;
            background-position: center;
		}
		h1{
			font-size:2.5rem;
			margin-top:100px;
			color:#ff523b;
			font-weight:800;
		}
		table
		{
			position: absolute;
			top:20%;
			left:20%;
			border-collapse:collapse;
			padding:10px;
			width:60%;
			color:black;
			border:5px solid #ff523b;
			font-family:calibri;
			background-color:white;

		}
		th
		{
			border: 2px solid black; 
			text-align:center;
			height:65px;
			font-size:25px;
			font-weight:bold;
			text-decoration:none;
			color:#ff523b;
			width:20%;
		}

		table td
		{
			border: 2px solid black; 
			text-align:center;
			height:62px;
			font-size:22px; 
			width:30px;
		}
</style>
</head>
<body>
	<h1 align="center">Xbox Games Info</h1>
	<table >
		<tr>
		<th>Name</th>
		<th>Image</th>
		<th>Rating</th>
		<th>Price</th>
		</tr>
		<xsl:for-each select="gamelist/game">
			<tr>
				<td><xsl:value-of select="name"/></td>
				<td><xsl:value-of select="img"/></td>
				<td><xsl:value-of select="rating"/></td>
				<td><xsl:value-of select="price"/></td>
			</tr>
		</xsl:for-each>
	</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>