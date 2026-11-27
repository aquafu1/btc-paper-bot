# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1618 windows, 38963 settled trades, 354 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 824 | 34.2 | 35.2 | $-651.33 | -7.9% | $348.67 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3841 | 50.8 | 50.0 | $-1017.14 | -2.6% | $-17.14 | -1.6 | done | can't tell from luck |
| value_ev10 | 1950 | 38.3 | 39.0 | $-1114.66 | -5.7% | $-114.66 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3214 | 51.1 | 50.9 | $-1472.89 | -4.6% | $-472.89 | -2.7 | done | losing for real |
| value_ev5 | 2917 | 40.3 | 41.0 | $-1554.04 | -5.3% | $-554.04 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3214 | 48.9 | 49.2 | $-1750.52 | -5.4% | $-750.52 | -3.1 | done | losing for real |
| trend_filter | 2284 | 48.5 | 50.4 | $-2028.85 | -8.9% | $-1028.85 | -4.3 | done | losing for real |
| coinflip | 5626 | 50.1 | 49.9 | $-2316.50 | -4.1% | $-1316.50 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3841 | 49.2 | 50.2 | $-2366.65 | -6.2% | $-1366.65 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5626 | 50.2 | 51.3 | $-3454.00 | -6.1% | $-2454.00 | -4.7 | done | losing for real |
| always_up | 5626 | 48.1 | 49.1 | $-3680.46 | -6.5% | $-2680.46 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10399 | 47.9 | 48.6 | $-5928.28 |
| ETH | 11254 | 48.0 | 47.7 | $-5894.52 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
