# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1422 windows, 36407 settled trades, 446 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 730 | 34.8 | 35.3 | $-465.63 | -6.4% | $534.37 | -1.3 | done | can't tell from luck |
| value_ev10 | 1764 | 38.9 | 39.2 | $-737.88 | -4.2% | $262.12 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3637 | 50.8 | 50.1 | $-1028.56 | -2.8% | $-28.56 | -1.7 | done | can't tell from luck |
| value_ev5 | 2664 | 40.7 | 41.1 | $-1202.32 | -4.5% | $-202.32 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3055 | 49.3 | 49.3 | $-1476.02 | -4.8% | $-476.02 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3055 | 50.7 | 50.9 | $-1576.99 | -5.2% | $-576.99 | -2.9 | done | losing for real |
| trend_filter | 2160 | 48.6 | 50.3 | $-1880.54 | -8.7% | $-880.54 | -4.1 | done | losing for real |
| coinflip | 5235 | 50.0 | 50.0 | $-2217.41 | -4.2% | $-1217.41 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3637 | 49.2 | 50.2 | $-2227.09 | -6.1% | $-1227.09 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5235 | 50.1 | 51.3 | $-3250.31 | -6.2% | $-2250.31 | -4.6 | done | losing for real |
| always_up | 5235 | 48.0 | 49.3 | $-3619.34 | -6.9% | $-2619.34 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9199 | 48.1 | 48.8 | $-4887.08 |
| ETH | 9898 | 48.1 | 48.0 | $-5210.78 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
