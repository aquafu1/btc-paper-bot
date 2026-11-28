# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1627 windows, 39079 settled trades, 352 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 829 | 34.4 | 35.2 | $-615.19 | -7.4% | $384.81 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3850 | 50.8 | 50.0 | $-1028.71 | -2.7% | $-28.71 | -1.7 | done | can't tell from luck |
| value_ev10 | 1958 | 38.3 | 39.0 | $-1108.52 | -5.7% | $-108.52 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3221 | 51.0 | 50.9 | $-1489.85 | -4.6% | $-489.85 | -2.7 | done | losing for real |
| value_ev5 | 2927 | 40.4 | 41.0 | $-1531.06 | -5.2% | $-531.06 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3221 | 49.0 | 49.2 | $-1744.92 | -5.4% | $-744.92 | -3.1 | done | losing for real |
| trend_filter | 2291 | 48.5 | 50.4 | $-2007.13 | -8.8% | $-1007.13 | -4.3 | done | losing for real |
| coinflip | 5644 | 50.1 | 49.9 | $-2336.57 | -4.1% | $-1336.57 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3850 | 49.2 | 50.2 | $-2346.42 | -6.1% | $-1346.42 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5644 | 50.2 | 51.3 | $-3397.38 | -6.0% | $-2397.38 | -4.7 | done | losing for real |
| always_up | 5644 | 48.2 | 49.1 | $-3581.90 | -6.3% | $-2581.90 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10449 | 48.0 | 48.6 | $-5835.09 |
| ETH | 11320 | 48.0 | 47.7 | $-5768.32 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
