# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 962 windows, 26658 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 491 | 35.0 | 34.8 | $-169.50 | -3.5% | $830.50 | -0.6 | done | can't tell from luck |
| value_ev10 | 1214 | 38.2 | 39.1 | $-639.76 | -5.3% | $360.24 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2722 | 51.4 | 50.5 | $-684.35 | -2.5% | $315.65 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2271 | 50.1 | 49.7 | $-911.20 | -4.0% | $88.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1842 | 40.0 | 41.0 | $-1000.59 | -5.4% | $-0.59 | -2.0 | done | can't tell from luck |
| trend_filter | 1593 | 49.9 | 50.9 | $-1063.19 | -6.7% | $-63.19 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2271 | 49.9 | 51.0 | $-1565.55 | -6.9% | $-565.55 | -3.4 | done | losing for real |
| coinflip | 3844 | 50.2 | 50.4 | $-1770.84 | -4.6% | $-770.84 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2722 | 48.6 | 50.3 | $-1951.37 | -7.2% | $-951.37 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3844 | 50.9 | 51.6 | $-1961.81 | -5.1% | $-961.81 | -3.3 | done | losing for real |
| always_up | 3844 | 47.0 | 49.6 | $-3711.44 | -9.7% | $-2711.44 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6072 | 48.2 | 49.0 | $-3469.07 |
| ETH | 6623 | 48.1 | 48.5 | $-4066.75 |
| SOL | 6964 | 48.3 | 48.6 | $-3714.75 |
| XRP | 6999 | 48.2 | 48.5 | $-4179.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
