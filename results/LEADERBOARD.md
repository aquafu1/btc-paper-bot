# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 658 windows, 18193 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1540 | 50.6 | 49.7 | $-384.06 | -2.5% | $615.94 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1866 | 51.6 | 50.9 | $-523.32 | -2.8% | $476.68 | -1.2 | done | can't tell from luck |
| trend_filter | 1056 | 50.5 | 51.0 | $-553.57 | -5.2% | $446.43 | -1.7 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2626 | 50.2 | 50.5 | $-1140.40 | -4.3% | $-140.40 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1540 | 49.4 | 51.3 | $-1220.45 | -7.9% | $-220.45 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1866 | 48.4 | 50.1 | $-1292.92 | -6.9% | $-292.92 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2626 | 50.8 | 51.8 | $-1388.78 | -5.3% | $-388.78 | -2.8 | done | losing for real |
| always_up | 2626 | 47.6 | 49.8 | $-2181.06 | -8.3% | $-1181.06 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4125 | 48.3 | 49.3 | $-2452.89 |
| ETH | 4534 | 48.3 | 48.7 | $-2766.74 |
| SOL | 4741 | 48.2 | 48.8 | $-2812.59 |
| XRP | 4793 | 48.6 | 48.6 | $-2225.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
