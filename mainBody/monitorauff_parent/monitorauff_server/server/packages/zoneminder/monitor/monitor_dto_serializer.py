from rest_framework import serializers


class MonitorDTOSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    notes = serializers.CharField()
    serverId = serializers.IntegerField()
    storageId = serializers.IntegerField()
    type = serializers.CharField()
    function = serializers.CharField()
    enabled = serializers.IntegerField()
    decodingEnabled = serializers.IntegerField()
    linkedMonitors = serializers.CharField()
    triggers = serializers.CharField()
    onvifURL = serializers.CharField()
    onvifUsername = serializers.CharField()
    onvifPassword = serializers.CharField()
    onvifOptions = serializers.CharField()
    device = serializers.CharField()
    channel = serializers.IntegerField()
    format = serializers.IntegerField()
    v4LMultiBuffer = serializers.CharField()
    v4LCapturesPerFrame = serializers.IntegerField()
    protocol = serializers.CharField()
    method = serializers.CharField()
    host = serializers.CharField()
    port = serializers.IntegerField()
    subPath = serializers.CharField()
    path = serializers.CharField()
    secondPath = serializers.CharField()
    options = serializers.CharField()
    user = serializers.CharField()
    password = serializers.CharField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    colours = serializers.IntegerField()
    palette = serializers.IntegerField()
    orientation = serializers.CharField()
    deinterlacing = serializers.IntegerField()
    decoderHWAccelName = serializers.CharField()
    decoderHWAccelDevice = serializers.CharField()
    saveJPEGs = serializers.IntegerField()
    videoWriter = serializers.IntegerField()
    outputCodec = serializers.IntegerField()
    encoder = serializers.CharField()
    outputContainer = serializers.CharField()
    encoderParameters = serializers.CharField()
    recordAudio = serializers.IntegerField()
    rtspDescribe: bool
    brightness = serializers.IntegerField()
    contrast = serializers.IntegerField()
    hue = serializers.IntegerField()
    colour = serializers.IntegerField()
    eventPrefix = serializers.CharField()
    labelFormat = serializers.CharField()
    labelX = serializers.IntegerField()
    labelY = serializers.IntegerField()
    labelSize = serializers.IntegerField()
    imageBufferCount = serializers.IntegerField()
    maxImageBufferCount = serializers.IntegerField()
    warmupCount = serializers.IntegerField()
    preEventCount = serializers.IntegerField()
    postEventCount = serializers.IntegerField()
    streamReplayBuffer = serializers.IntegerField()
    alarmFrameCount = serializers.IntegerField()
    sectionLength = serializers.IntegerField()
    minSectionLength = serializers.IntegerField()
    frameSkip = serializers.IntegerField()
    motionFrameSkip = serializers.IntegerField()
    analysisFPSLimit = serializers.CharField()
    analysisUpdateDelay = serializers.IntegerField()
    maxFPS = serializers.CharField()
    alarmMaxFPS = serializers.CharField()
    fpsReportInterval = serializers.IntegerField()
    refBlendPerc = serializers.IntegerField()
    alarmRefBlendPerc = serializers.IntegerField()
    controllable = serializers.IntegerField()
    controlId = serializers.CharField()
    controlDevice = serializers.CharField()
    controlAddress = serializers.CharField()
    autoStopTimeout = serializers.CharField()
    trackMotion = serializers.IntegerField()
    trackDelay = serializers.CharField()
    returnLocation = serializers.IntegerField()
    returnDelay = serializers.CharField()
    modectDuringPTZ = serializers.IntegerField()
    defaultRate = serializers.IntegerField()
    defaultScale = serializers.IntegerField()
    defaultCodec = serializers.CharField()
    signalCheckPoints = serializers.IntegerField()
    signalCheckColour = serializers.CharField()
    webColour = serializers.CharField()
    exif: bool
    sequence = serializers.IntegerField()
    zoneCount = serializers.IntegerField()
    refresh = serializers.CharField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    rtspServer: bool
    rtspStreamName = serializers.CharField()
    importance = serializers.CharField()
