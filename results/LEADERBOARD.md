# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 483 windows, 13269 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 242 | 35.1 | 35.8 | $-122.29 | -5.1% | $877.71 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1126 | 51.0 | 49.8 | $-183.09 | -1.6% | $816.91 | -0.5 | done | can't tell from luck |
| value_ev10 | 623 | 39.2 | 40.1 | $-333.65 | -5.4% | $666.35 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1340 | 50.2 | 50.0 | $-396.29 | -3.0% | $603.71 | -1.1 | done | can't tell from luck |
| value_ev5 | 921 | 41.2 | 41.8 | $-449.82 | -4.9% | $550.18 | -1.3 | done | can't tell from luck |
| trend_filter | 776 | 49.5 | 50.7 | $-503.93 | -6.5% | $496.07 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1340 | 49.8 | 51.5 | $-978.14 | -7.3% | $21.86 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1126 | 49.0 | 51.6 | $-1013.68 | -9.0% | $-13.68 | -3.1 | done | losing for real |
| coinflip | 1925 | 49.9 | 50.8 | $-1020.33 | -5.3% | $-20.33 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1925 | 49.6 | 51.7 | $-1427.24 | -7.4% | $-427.24 | -3.4 | done | losing for real |
| always_up | 1925 | 46.4 | 50.4 | $-2223.30 | -11.5% | $-1223.30 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2991 | 47.4 | 49.3 | $-2327.15 |
| ETH | 3323 | 48.2 | 48.9 | $-2061.68 |
| SOL | 3452 | 47.8 | 49.3 | $-2434.00 |
| XRP | 3503 | 48.5 | 49.0 | $-1828.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
