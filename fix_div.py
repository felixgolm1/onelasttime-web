import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    )}"""

replacement = """                                                </div>
                                            </div>
                                        </div>
                                    )}"""
text = text.replace(target, replacement, 1)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Removed extra div!")

