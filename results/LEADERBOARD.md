# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1349 windows, 35371 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 698 | 34.1 | 35.4 | $-568.07 | -8.1% | $431.93 | -1.6 | done | can't tell from luck |
| value_ev10 | 1707 | 38.7 | 39.2 | $-854.05 | -5.0% | $145.95 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3538 | 50.8 | 50.1 | $-1043.33 | -2.9% | $-43.33 | -1.8 | done | can't tell from luck |
| value_ev5 | 2576 | 40.4 | 41.1 | $-1371.12 | -5.3% | $-371.12 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2973 | 49.4 | 49.5 | $-1455.27 | -4.9% | $-455.27 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2973 | 50.6 | 50.9 | $-1567.49 | -5.3% | $-567.49 | -2.9 | done | losing for real |
| trend_filter | 2104 | 48.7 | 50.5 | $-1809.16 | -8.6% | $-809.16 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3538 | 49.2 | 50.3 | $-2209.90 | -6.2% | $-1209.90 | -3.8 | done | losing for real |
| coinflip | 5088 | 49.9 | 50.1 | $-2326.43 | -4.6% | $-1326.43 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5088 | 50.3 | 51.4 | $-3056.04 | -6.0% | $-2056.04 | -4.4 | done | losing for real |
| always_up | 5088 | 47.9 | 49.3 | $-3717.47 | -7.3% | $-2717.47 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8688 | 47.8 | 48.8 | $-5367.21 |
| ETH | 9373 | 48.2 | 48.2 | $-5026.90 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
