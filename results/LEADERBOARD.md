# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1337 windows, 35198 settled trades, 418 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 694 | 34.3 | 35.4 | $-528.07 | -7.6% | $471.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1696 | 38.7 | 39.2 | $-820.05 | -4.8% | $179.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3525 | 50.9 | 50.2 | $-979.25 | -2.8% | $20.75 | -1.6 | done | can't tell from luck |
| value_ev5 | 2560 | 40.4 | 41.1 | $-1323.07 | -5.2% | $-323.07 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2956 | 49.3 | 49.5 | $-1462.55 | -4.9% | $-462.55 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2956 | 50.7 | 50.9 | $-1515.83 | -5.1% | $-515.83 | -2.8 | done | losing for real |
| trend_filter | 2094 | 48.7 | 50.5 | $-1792.68 | -8.6% | $-792.68 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3525 | 49.1 | 50.2 | $-2250.07 | -6.4% | $-1250.07 | -3.8 | done | losing for real |
| coinflip | 5064 | 49.9 | 50.1 | $-2343.32 | -4.6% | $-1343.32 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5064 | 50.3 | 51.4 | $-3010.92 | -5.9% | $-2010.92 | -4.4 | done | losing for real |
| always_up | 5064 | 47.9 | 49.3 | $-3628.92 | -7.2% | $-2628.92 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8611 | 47.9 | 48.9 | $-5213.36 |
| ETH | 9277 | 48.2 | 48.2 | $-4857.13 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
