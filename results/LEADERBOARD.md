# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1400 windows, 36091 settled trades, 395 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 724 | 34.7 | 35.4 | $-493.87 | -6.8% | $506.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1749 | 38.9 | 39.2 | $-768.67 | -4.4% | $231.33 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3606 | 50.9 | 50.1 | $-1001.50 | -2.8% | $-1.50 | -1.7 | done | can't tell from luck |
| value_ev5 | 2637 | 40.6 | 41.1 | $-1250.13 | -4.7% | $-250.13 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3027 | 49.3 | 49.3 | $-1474.96 | -4.9% | $-474.96 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3027 | 50.7 | 50.9 | $-1567.67 | -5.2% | $-567.67 | -2.9 | done | losing for real |
| trend_filter | 2145 | 48.5 | 50.4 | $-1891.37 | -8.8% | $-891.37 | -4.2 | done | losing for real |
| coinflip | 5190 | 50.1 | 50.0 | $-2207.42 | -4.3% | $-1207.42 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3606 | 49.1 | 50.2 | $-2257.92 | -6.3% | $-1257.92 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5190 | 50.2 | 51.3 | $-3211.95 | -6.2% | $-2211.95 | -4.6 | done | losing for real |
| always_up | 5190 | 47.9 | 49.3 | $-3713.94 | -7.2% | $-2713.94 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9046 | 48.1 | 48.8 | $-4982.01 |
| ETH | 9735 | 48.1 | 48.1 | $-5273.16 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
