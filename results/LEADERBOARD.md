# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 447 windows, 12280 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 226 | 34.5 | 36.0 | $-169.66 | -7.5% | $830.34 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1046 | 51.2 | 50.0 | $-192.78 | -1.8% | $807.22 | -0.6 | done | can't tell from luck |
| trend_filter | 708 | 50.0 | 50.7 | $-385.52 | -5.4% | $614.48 | -1.5 | done | can't tell from luck |
| value_ev10 | 577 | 38.5 | 40.1 | $-435.06 | -7.5% | $564.94 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1240 | 49.8 | 50.0 | $-523.57 | -4.2% | $476.43 | -1.5 | done | can't tell from luck |
| value_ev5 | 857 | 40.8 | 41.8 | $-529.74 | -6.2% | $470.26 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1240 | 50.2 | 51.6 | $-867.00 | -7.0% | $133.00 | -2.6 | done | losing for real |
| coinflip | 1780 | 50.0 | 50.8 | $-966.82 | -5.4% | $33.18 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1046 | 48.8 | 51.7 | $-1047.00 | -10.0% | $-47.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1780 | 49.5 | 51.5 | $-1355.69 | -7.6% | $-355.69 | -3.3 | done | losing for real |
| always_up | 1780 | 45.9 | 50.5 | $-2316.78 | -13.0% | $-1316.78 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2771 | 47.6 | 49.3 | $-2180.56 |
| ETH | 3085 | 47.8 | 48.8 | $-2121.37 |
| SOL | 3191 | 47.6 | 49.3 | $-2620.61 |
| XRP | 3233 | 48.5 | 49.2 | $-1867.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
