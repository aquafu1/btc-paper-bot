# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 7:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 956 windows, 26505 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 487 | 35.1 | 34.9 | $-154.35 | -3.2% | $845.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1203 | 38.1 | 39.1 | $-672.83 | -5.6% | $327.17 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2708 | 51.3 | 50.6 | $-778.27 | -2.9% | $221.73 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2266 | 50.2 | 49.7 | $-861.20 | -3.8% | $138.80 | -1.8 | done | can't tell from luck |
| trend_filter | 1586 | 50.0 | 50.8 | $-1025.59 | -6.5% | $-25.59 | -2.6 | done | losing for real |
| value_ev5 | 1827 | 39.9 | 41.0 | $-1042.67 | -5.7% | $-42.67 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2266 | 49.8 | 51.0 | $-1643.92 | -7.3% | $-643.92 | -3.5 | done | losing for real |
| coinflip | 3818 | 50.2 | 50.4 | $-1727.03 | -4.5% | $-727.03 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2708 | 48.7 | 50.2 | $-1873.92 | -6.9% | $-873.92 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3818 | 50.9 | 51.5 | $-1932.78 | -5.1% | $-932.78 | -3.2 | done | losing for real |
| always_up | 3818 | 46.8 | 49.6 | $-3776.34 | -9.9% | $-2776.34 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6041 | 48.2 | 49.0 | $-3453.71 |
| ETH | 6581 | 48.2 | 48.5 | $-4014.28 |
| SOL | 6919 | 48.2 | 48.6 | $-3839.99 |
| XRP | 6964 | 48.2 | 48.5 | $-4180.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
