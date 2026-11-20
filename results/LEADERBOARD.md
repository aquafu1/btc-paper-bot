# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 928 windows, 25638 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2185 | 50.1 | 49.8 | $-903.51 | -4.1% | $96.49 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2615 | 50.7 | 50.5 | $-975.81 | -3.7% | $24.19 | -1.9 | done | can't tell from luck |
| value_ev5 | 1763 | 39.8 | 41.0 | $-1047.33 | -5.9% | $-47.33 | -2.1 | done | losing for real |
| trend_filter | 1527 | 49.9 | 51.0 | $-1065.88 | -7.0% | $-65.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2185 | 49.9 | 50.9 | $-1517.24 | -6.9% | $-517.24 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2615 | 49.3 | 50.3 | $-1527.33 | -5.8% | $-527.33 | -3.0 | done | losing for real |
| coinflip | 3704 | 50.4 | 50.3 | $-1556.74 | -4.2% | $-556.74 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3704 | 50.9 | 51.6 | $-1889.98 | -5.1% | $-889.98 | -3.2 | done | losing for real |
| always_up | 3704 | 46.8 | 49.7 | $-3782.67 | -10.2% | $-2782.67 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5837 | 48.2 | 49.1 | $-3362.30 |
| ETH | 6378 | 48.2 | 48.6 | $-3980.88 |
| SOL | 6690 | 48.1 | 48.6 | $-3916.39 |
| XRP | 6733 | 48.3 | 48.5 | $-3785.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
