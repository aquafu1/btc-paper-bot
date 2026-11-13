# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 202 windows, 5241 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 515 | 57.5 | 52.7 | $+290.73 | +5.6% | $1290.73 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 394 | 56.6 | 52.9 | $+136.83 | +3.5% | $1136.83 | +0.7 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 7:00 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 802 | 51.1 | 51.4 | $-382.92 | -4.8% | $617.08 | -1.4 | done | can't tell from luck |
| trend_filter | 268 | 43.7 | 49.7 | $-421.92 | -15.7% | $578.08 | -2.6 | done | losing for real |
| coinflip | 802 | 50.4 | 51.0 | $-477.80 | -6.0% | $522.20 | -1.8 | done | can't tell from luck |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| value_ev5 | 386 | 37.8 | 42.7 | $-615.55 | -15.9% | $384.45 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 394 | 43.4 | 49.4 | $-643.13 | -16.3% | $356.87 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 515 | 42.5 | 49.6 | $-920.39 | -17.9% | $79.61 | -4.1 | done | losing for real |
| always_up | 802 | 45.3 | 50.3 | $-1171.58 | -14.6% | $-171.58 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1155 | 45.8 | 49.6 | $-1303.04 |
| ETH | 1301 | 46.0 | 48.9 | $-1504.40 |
| SOL | 1361 | 47.5 | 49.2 | $-1297.26 |
| XRP | 1424 | 49.0 | 49.3 | $-833.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
