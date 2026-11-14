# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 300 windows, 8001 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 148 | 35.1 | 36.5 | $-134.69 | -9.1% | $865.31 | -0.9 | Sun 2:45 AM | too few trades (148/200) |
| reversal_15m_0.10pct | 795 | 53.0 | 51.9 | $-179.78 | -2.3% | $820.22 | -0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 650 | 52.5 | 51.9 | $-214.68 | -3.3% | $785.32 | -0.9 | done | can't tell from luck |
| value_ev10 | 383 | 38.4 | 40.5 | $-361.48 | -9.4% | $638.52 | -1.6 | done | can't tell from luck |
| value_ev5 | 565 | 40.2 | 42.2 | $-522.78 | -9.3% | $477.22 | -1.9 | done | can't tell from luck |
| trend_filter | 439 | 46.2 | 50.3 | $-553.62 | -12.6% | $446.38 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 650 | 47.5 | 49.8 | $-614.60 | -9.5% | $385.40 | -2.5 | done | losing for real |
| coinflip | 1192 | 50.2 | 50.9 | $-679.62 | -5.7% | $320.38 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 795 | 47.0 | 49.9 | $-785.12 | -9.9% | $214.88 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1192 | 49.2 | 51.4 | $-1000.16 | -8.4% | $-0.16 | -3.0 | done | losing for real |
| always_up | 1192 | 47.3 | 50.3 | $-1208.47 | -10.1% | $-208.47 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1790 | 46.8 | 49.4 | $-1669.43 |
| ETH | 2004 | 47.2 | 48.8 | $-1834.41 |
| SOL | 2078 | 48.4 | 49.4 | $-1559.44 |
| XRP | 2129 | 48.6 | 49.1 | $-1191.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
