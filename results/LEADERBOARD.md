# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 339 windows, 9066 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 4:30 PM | too few trades (184/200) |
| reversal_60m_0.30pct | 725 | 53.0 | 51.9 | $-146.69 | -2.0% | $853.31 | -0.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 898 | 52.4 | 51.9 | $-290.13 | -3.2% | $709.87 | -1.0 | done | can't tell from luck |
| value_ev10 | 443 | 39.1 | 40.2 | $-295.27 | -6.7% | $704.73 | -1.2 | done | can't tell from luck |
| value_ev5 | 657 | 40.6 | 41.9 | $-459.71 | -7.0% | $540.29 | -1.6 | done | can't tell from luck |
| trend_filter | 492 | 45.7 | 50.3 | $-659.95 | -13.4% | $340.05 | -3.0 | done | losing for real |
| coinflip | 1348 | 50.1 | 50.8 | $-719.90 | -5.3% | $280.10 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 725 | 47.0 | 49.7 | $-724.25 | -10.0% | $275.75 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 898 | 47.6 | 49.8 | $-786.45 | -8.8% | $213.55 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 1348 | 48.8 | 51.3 | $-1176.94 | -8.7% | $-176.94 | -3.3 | done | losing for real |
| always_up | 1348 | 47.3 | 50.5 | $-1361.84 | -10.1% | $-361.84 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2028 | 46.9 | 49.2 | $-1752.15 |
| ETH | 2280 | 47.4 | 48.6 | $-1760.23 |
| SOL | 2357 | 47.9 | 49.3 | $-1853.35 |
| XRP | 2401 | 48.7 | 49.1 | $-1293.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
