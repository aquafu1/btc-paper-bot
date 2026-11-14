# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 343 windows, 9192 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 5:30 PM | too few trades (184/200) |
| value_ev10 | 449 | 39.9 | 40.2 | $-206.45 | -4.6% | $793.55 | -0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 741 | 51.8 | 52.0 | $-306.69 | -4.1% | $693.31 | -1.2 | done | can't tell from luck |
| value_ev5 | 665 | 41.4 | 41.9 | $-349.72 | -5.3% | $650.28 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 909 | 51.8 | 51.9 | $-400.13 | -4.4% | $599.87 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 741 | 48.2 | 49.6 | $-527.97 | -7.1% | $472.03 | -2.0 | done | can't tell from luck |
| trend_filter | 502 | 46.8 | 50.2 | $-541.84 | -10.8% | $458.16 | -2.5 | done | losing for real |
| coinflip | 1364 | 50.4 | 50.8 | $-636.77 | -4.7% | $363.23 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 909 | 48.2 | 49.8 | $-648.97 | -7.1% | $351.03 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1364 | 49.0 | 51.3 | $-1118.83 | -8.2% | $-118.83 | -3.1 | done | losing for real |
| always_up | 1364 | 46.8 | 50.6 | $-1521.84 | -11.2% | $-521.84 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2060 | 47.1 | 49.3 | $-1661.76 |
| ETH | 2312 | 47.5 | 48.6 | $-1686.95 |
| SOL | 2388 | 48.0 | 49.3 | $-1747.64 |
| XRP | 2432 | 48.8 | 49.1 | $-1201.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
