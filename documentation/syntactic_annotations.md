# Syntactic Annoations

The CELER data is released along with syntactic annotations (manual annotations for WSJ PTB sentences (v1), and automatic for BLLIP sentences (new to v2)).

The annotations are available in the `annotations` folder, where each file prefix is a list number, and the file contains annotations for the individual regime sentences of that list. List 0 contains annotations of the shared regime sentences.

- `.ids` sentence ids
- `.trees` phrase structure trees (taken from WSJ PTB and BLLIP)
- `.conllu` dependency trees and Google universal POS tags obtained using the converstion tool of the Universal Dependency Treebank (UDT, McDonald et al. 2013).Note that this annotation scheme is outdated. We recommend using instead the current stadard of Universal Dependencies (UD) annotations. 