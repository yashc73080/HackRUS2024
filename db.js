const fs = require("fs");
require("dotenv").config();
const { MongoClient, ServerApiVersion } = require("mongodb");
var uri = `mongodb+srv://${process.env.MONGODB_CLI_USERNAME}:` +
            `${process.env.MONGODB_CLI_PASSWORD}` +
            "@betterrutgerssoc.emmh2hn.mongodb.net/?retryWrites=true&w=majority";