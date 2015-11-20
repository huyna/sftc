__author__ = 'HuyNA'
"""
    While the implementation should be fairly compliant, it does assume it is given valid compressed data,
    and that there is sufficient space for the decompressed data.

Twenty Lines of Buttpain.

nc 109.233.61.11 2020

Flag format: CTF{..32 hexes..}

+) In computing, deflate is a data compression algorithm that uses a combination of the LZ77 algorithm and Huffman coding.
It was originally defined by Phil Katz for version 2 of his PKZIP archiving tool and was later specified in RFC 1951.

+)A Deflate stream consists of a series of blocks. Each block is preceded by a 3-bit header:
First bit: Last-block-in-stream marker:
    1: this is the last block in the stream.
    0: there are more blocks to process after this one.
Second and third bits: Encoding method used for this block type:
    00: a stored/raw/literal section, between 0 and 65,535 bytes in length.
    01: a static Huffman compressed block, using a pre-agreed Huffman tree.
    10: a compressed block complete with the Huffman table supplied.
    11: reserved, don't use.

Inflate RFC: http://www.rfc-editor.org/rfc/rfc1951.txt

"""

print('a'*10000)