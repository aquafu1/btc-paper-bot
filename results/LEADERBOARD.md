# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 117 windows, 2997 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 288 | 56.2 | 51.8 | $+184.19 | +6.4% | $1184.19 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 461 | 52.3 | 50.8 | $-48.80 | -1.1% | $951.20 | -0.2 | done | can't tell from luck |
| value_ev10 | 157 | 39.5 | 40.5 | $-108.93 | -6.9% | $891.07 | -0.7 | Thu 7:30 AM | too few trades (157/200) |
| value_ev20 | 58 | 27.6 | 36.5 | $-152.65 | -26.3% | $847.35 | -1.6 | Sun 4:00 AM | too few trades (58/200) |
| value_ev5 | 220 | 38.2 | 41.9 | $-279.87 | -12.7% | $720.13 | -1.7 | done | can't tell from luck |
| coinflip | 461 | 50.1 | 51.2 | $-282.25 | -6.1% | $717.75 | -1.4 | done | can't tell from luck |
| trend_filter | 155 | 40.6 | 48.7 | $-297.88 | -19.2% | $702.12 | -2.4 | Thu 8:00 AM | too few trades (155/200) |
| momentum_15m_0.10pct | 288 | 43.8 | 50.3 | $-451.58 | -15.7% | $548.42 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |
| always_up | 461 | 46.0 | 50.4 | $-575.98 | -12.5% | $424.02 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 649 | 45.6 | 49.6 | $-641.86 |
| ETH | 730 | 45.2 | 48.9 | $-764.94 |
| SOL | 798 | 48.0 | 48.5 | $-591.28 |
| XRP | 820 | 50.2 | 48.9 | $-232.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
