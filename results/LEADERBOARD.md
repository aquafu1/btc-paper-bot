# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 613 windows, 16922 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1427 | 51.2 | 49.7 | $-200.23 | -1.4% | $799.77 | -0.5 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| trend_filter | 974 | 50.4 | 51.0 | $-536.92 | -5.5% | $463.08 | -1.8 | done | can't tell from luck |
| value_ev10 | 789 | 38.1 | 39.4 | $-571.87 | -7.2% | $428.13 | -1.7 | done | can't tell from luck |
| value_ev5 | 1188 | 40.4 | 41.3 | $-724.88 | -6.1% | $275.12 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1729 | 50.7 | 50.9 | $-810.28 | -4.7% | $189.72 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1729 | 49.3 | 50.1 | $-967.85 | -5.6% | $32.15 | -2.3 | done | losing for real |
| coinflip | 2444 | 50.0 | 50.5 | $-1210.37 | -5.0% | $-210.37 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1427 | 48.8 | 51.3 | $-1351.79 | -9.5% | $-351.79 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2444 | 50.4 | 51.8 | $-1549.35 | -6.3% | $-549.35 | -3.3 | done | losing for real |
| always_up | 2444 | 46.9 | 49.8 | $-2386.65 | -9.8% | $-1386.65 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3845 | 48.0 | 49.2 | $-2540.55 |
| ETH | 4234 | 48.0 | 48.6 | $-2769.97 |
| SOL | 4393 | 47.9 | 48.8 | $-2937.07 |
| XRP | 4450 | 48.5 | 48.6 | $-2307.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
