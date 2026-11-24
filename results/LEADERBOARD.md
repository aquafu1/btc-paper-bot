# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 4:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1281 windows, 34359 settled trades, 410 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 675 | 33.9 | 35.3 | $-560.36 | -8.3% | $439.64 | -1.6 | done | can't tell from luck |
| value_ev10 | 1650 | 38.5 | 39.2 | $-860.65 | -5.2% | $139.35 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3446 | 50.7 | 50.2 | $-1184.42 | -3.4% | $-184.42 | -2.0 | done | losing for real |
| value_ev5 | 2493 | 40.4 | 41.1 | $-1312.01 | -5.3% | $-312.01 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2880 | 49.5 | 49.4 | $-1339.08 | -4.6% | $-339.08 | -2.5 | done | losing for real |
| trend_filter | 2033 | 49.0 | 50.5 | $-1623.73 | -8.0% | $-623.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2880 | 50.5 | 51.0 | $-1663.39 | -5.8% | $-663.39 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3446 | 49.3 | 50.3 | $-2068.38 | -6.0% | $-1068.38 | -3.6 | done | losing for real |
| coinflip | 4952 | 49.9 | 50.1 | $-2305.37 | -4.7% | $-1305.37 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4952 | 50.5 | 51.4 | $-2785.68 | -5.6% | $-1785.68 | -4.1 | done | losing for real |
| always_up | 4952 | 47.8 | 49.3 | $-3660.09 | -7.4% | $-2660.09 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8199 | 48.0 | 48.8 | $-4912.49 |
| ETH | 8850 | 48.2 | 48.2 | $-4866.44 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
