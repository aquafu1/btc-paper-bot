# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1216 windows, 33400 settled trades, 342 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1597 | 38.8 | 39.2 | $-766.01 | -4.8% | $233.99 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3347 | 50.8 | 50.3 | $-1094.90 | -3.3% | $-94.90 | -1.9 | done | can't tell from luck |
| value_ev5 | 2415 | 40.5 | 41.1 | $-1181.23 | -4.9% | $-181.23 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2801 | 49.6 | 49.4 | $-1256.35 | -4.5% | $-256.35 | -2.4 | done | losing for real |
| trend_filter | 1974 | 48.7 | 50.4 | $-1666.56 | -8.4% | $-666.56 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2801 | 50.4 | 51.1 | $-1679.23 | -6.0% | $-679.23 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3347 | 49.2 | 50.2 | $-2043.85 | -6.1% | $-1043.85 | -3.6 | done | losing for real |
| coinflip | 4822 | 50.0 | 50.1 | $-2191.60 | -4.5% | $-1191.60 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4822 | 50.2 | 51.4 | $-2939.92 | -6.1% | $-1939.92 | -4.4 | done | losing for real |
| always_up | 4822 | 47.8 | 49.3 | $-3548.75 | -7.4% | $-2548.75 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7735 | 48.1 | 48.9 | $-4290.92 |
| ETH | 8355 | 48.1 | 48.3 | $-4936.71 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
